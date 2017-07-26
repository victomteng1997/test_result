function [ answer ] = Gra_Dev_Group_delay( num,den,num_sam,initial,tau)
% Calculate the gradient of deviation of group delay
%the final result would be an huge matrix, m*n
%n would be the sum of length num and length den
%m would be num_sam

%every column is the gradient of deviation of group delay at that specific
%frequency (based on num sum)
[gd,w] = grpdelay(num,den,num_sam);
matrix = zeros(num_sam,1);
matrix(:,:) = tau;
answer = [];
for i = 1:length(num)             %firstly calculate num gradient
    num(i) = num(i) + 0.0001;
    [new,w] = grpdelay(num,den,num_sam);
    num(i) = num(i) - 0.0001;
    dev = (new - matrix-initial)/0.0001;
    answer = [answer,dev];
end
for i = 1:length(den)             %Then calculate den gradient
    den(i) = den(i) + 0.0001;
    [new,w] = grpdelay(num,den,num_sam);
    den(i) = den(i) - 0.0001;
    dev = (new - matrix-initial)/0.0001;
    answer = [answer,dev];
end

% A very important idea here:
%{
Put sensitivity map here.
%}

end

