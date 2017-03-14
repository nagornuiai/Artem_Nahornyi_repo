function [J grad] = cost_func(theta, X, y, lambda)

m = length(y);
%g_of_z = 1/(1+e^-(X*theta))
%reg_el = lambda/(2*m) * sum(theta(2:end))
grad = zeros(1,length(theta));

%J = 1/m * sum(-y .* log(1./(1.+e.^-(X*theta))) - (1-y).*log(1-1./(1.+e.^-(X*theta)))) + lambda/(2*m) * sum(theta(2:end).^2);
J = (1/m)*sum(-y.*log(1./(1.+e.^-(X*theta))) -(1.-y).*log(1 .- 1./(1.+e.^-(X*theta)))) + lambda/(2*m) * sum(theta(2:end).^2);
%J = (1/m)*sum(-y.*log(1./(1.+e.^-(X*theta))) -(1.-y).*log(1 .- 1./(1.+e.^-(X*theta)))) + lambda/(2*m) * sum(theta(2:end).^2);

grad(1) = 1/m * sum((1./(1+e.^-(X*theta)) - y) .* X(:,1)) ;
grad(2:end) = 1/m * transpose( transpose(1/m *sum( (1./(1.+e.^-(X*theta)) - y) .*X(:,2:end))) + (lambda/m)*theta(2:end)) ;   



end