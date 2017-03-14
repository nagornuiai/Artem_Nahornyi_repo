function J = cost_func(X, y, theta, lambda)

m = length(y);
%g_of_z = 1/(1+e^-(X*theta))
%reg_el = lambda/(2*m) * sum(theta(2:end))

J = 1/m * sum(-y .* log(1./(1.+e.^-(X*theta))) - (1-y).*log(1-1./(1.+e.^-(X*theta)))) + lambda/(2*m) * sum(theta(2:end).^2);
%J = (1/m)*sum(-y.*log(1./(1.+e.^-(X*theta))) -(1.-y).*log(1 .- 1./(1.+e.^-(X*theta)))) + lambda/(2*m) * sum(theta(2:end).^2);


end