function [X_norm mu sigma] = setNormalize(X)

mu = mean(X);
sigma = std(X);
X_norm = (X.-mu)./sigma;

end