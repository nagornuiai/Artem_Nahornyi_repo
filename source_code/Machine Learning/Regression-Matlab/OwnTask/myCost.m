function J = myCost(X, y, theta)

J = (1/(2*length(y))) * sum((X*theta .-y).^2);

end