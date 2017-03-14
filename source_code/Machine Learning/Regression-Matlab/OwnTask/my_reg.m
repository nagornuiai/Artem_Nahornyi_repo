function [theta, J_hist] = my_reg(X, y, theta, alpha, num_iter, J)

J_hist = zeros(num_iter, 1);


for i = 1:num_iter

theta = theta - transpose(alpha*(1/length(y))*sum((X*theta .- y).*X));

J_hist(i) = myCost(X, y, theta);

end
disp(i)
disp(theta)





end