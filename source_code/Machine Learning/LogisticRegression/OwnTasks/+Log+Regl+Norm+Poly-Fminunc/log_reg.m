close all; clear; clc;
data_scource_file = input('Enter file name:', 's');

data = load(data_scource_file);

X = data(:,1:6);
y = data(:,7);

[X mu sigma] = norm_func(X);

X = [ones(length(y),1), X];
alpha = 0.1;
lambda = 0;
initial_theta = zeros(size(X)(2),1);
max_iter = input('How many iterations does Gradiend Descent should perform?:');

[J_hist theta] = reg_func(X, y, initial_theta, alpha, lambda, max_iter);

plot(1:max_iter, J_hist, 'ko', 'MarkerFaceColor', 'g')