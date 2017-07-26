function [ result ] = to_dec( num )
% binary to decimal
%   此处显示详细说明
p=0;
result = 0;
if num(1) == '-'
    num = num(2:length(num));
    p = 1;
end
for i = 1:length(num)
    if num(i) == '.'
        k = i;
    end
end
for i = 1:k
    if num(i) == '1';
        result = result + 2^(k-i-1);
    end
end
for i = k+1:length(num);
    if num(i) == '1'
        result = result + 2^(k-i);
    end
end
if p ==1
    result = 0-result;
end
end

