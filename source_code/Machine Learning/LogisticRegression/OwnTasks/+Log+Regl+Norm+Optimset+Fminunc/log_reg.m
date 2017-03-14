close all; clear; clc;
data_scource_file = input('Enter file name:', 's');

data = load(data_scource_file);

X = data(:,1:6);
y = data(:,7);

[X mu sigma] = norm_func(X);

X = [ones(length(y),1), X];
alpha = 0.1;
lambda = 0;
max_iter = 400;
initial_theta = zeros(size(X)(2),1);

[cost grad] = cost_func(initial_theta, X, y, lambda);

options = optimset('GradObj', 'on', 'MaxIter', 400);

[theta, J, exit_flag] = fminunc(@(t)(cost_func(t, X, y, lambda)), initial_theta, options);

plot(1:max_iter, J, 'ko', 'MarkerFaceColor', 'g');