function [J_hist theta] = reg_func(X, y, theta, alpha, lambda, max_iter)
J_hist = [];
m = length(y);
theta_i = theta
for i = 1:max_iter

theta_i(1) = theta(1) - alpha/m * sum((1./(1+e.^-(X*theta)) - y) .* X(:,1)) ;
theta_i(2:end) = theta(2:end) - alpha * ( transpose(1/m *sum( (1./(1.+e.^-(X*theta)) - y) .*X(:,2:end))) + (lambda/m)*theta(2:end)) ;   
theta = theta_i


J_hist = [J_hist, cost_func(X, y, theta, lambda)];

end
end