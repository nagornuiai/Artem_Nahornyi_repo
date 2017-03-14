clear all; clear; clc;
data = load('ex1data2.txt');
X = data(:,1:2);
y = data(:,3);

[X mu sigma] = setNormalize(X);

X = [ones(length(y),1), X];

theta = zeros(size(X,2),1);
num_iter = 400;
alpha = 0.1;

[theta J_hist] = my_reg(X, y, theta, alpha, num_iter);

figure 1;
ylabel('Cost');
xlabel('iterations');
plot(1:num_iter, J_hist);


new_case = input('Enter you Xs: \n >>');
new_case = (new_case.- mu)./sigma;
Xs = [ones(size(new_case,1), 1), new_case];
prediction = Xs * theta;

disp('price: $'); disp(prediction);