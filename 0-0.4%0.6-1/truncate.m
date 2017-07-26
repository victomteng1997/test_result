function [ result ] = truncate(vector, k)
% truncate a vector coeff into k th word length
%   �˴���ʾ��ϸ˵��
len = length(vector);
result = zeros(1,len);
for i = 1:len
    binary= to_binary(vector(i),k);
    result(i) = to_dec(binary);
end
end

