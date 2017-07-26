function [result] = to_binary(vec,n)
% turn all the numbers in the vector into binary numbers
% digits of binary number can be set by n.

%{
format is recoreded in this way:
                                  coe1  coe2 .......
int part: p or n                [  1    (0 represents positive, 1
negative)                          n    (position of decimal point, 


(for example, if the decimal number is 15.3233, the binary result should be

0 4 1 1 1 1 0 1 ....... 4 represents that the decimal number is after the
fourth binary digit, which is the "1" at the fourth position, so the binary
number should be 1111.01.......
                                                                

                                                                        ]
%}

len = length(vec);
result = zeros(n+2,len);
for c = 1:len
    data = vec(c);
    if data > 0
        int_part = floor(data);
    else
        data = 0-data;
        int_part = floor(data);
        result(1,c) = 1;
    end
    
    dec_part = data - int_part;
    int_bi = de2bi(int_part)';
    result(2,c) = length(int_bi);
    result(3:(length(int_bi)+2),c) = int_bi;
    
    for i = length(int_bi)+3:n+2
        result(i,c) = floor(dec_part*2);
        dec_part = dec_part*2-floor(dec_part*2);
        
    end
end
end

