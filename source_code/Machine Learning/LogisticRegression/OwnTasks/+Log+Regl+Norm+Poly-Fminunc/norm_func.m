function [X_norm mu sigma] = norm_func(X)

mu = mean(X);
sigma = std(X);

X_norm = (X .- mu) ./ sigma;

end