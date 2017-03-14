function [esteem_matrix] = predict(X, y, theta)

w_matrix = X*theta;
pos = find(w_matrix >= 0);
neg = find(w_matrix < 0);
w_matrix(pos) = 1;
w_matrix(neg) = 0;

esteem_matrix = [X, w_matrix, y]; %9
n_match = find(esteem_matrix(:,end-1) == esteem_matrix(:,end));

m = length(y);
n = length(n_match);

accuracy = n/m


end