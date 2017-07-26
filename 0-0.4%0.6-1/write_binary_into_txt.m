function [ result ] = write_binary_into_txt( vector )
%   For a vector that contains binary coefficients, this function will
%   write the binary coefficients into a txt file
%   One thing to notice, the vector contains every single coeff in a
%   column, while the txt file contains every single coeff in a row.

dimension = size(vector);
vector = vector(2:dimension(1),:);
dimension = size(vector);
fid = fopen('coeff.txt','w');
for m = 1:dimension(2)
    for n = 1:dimension(1)
        fprintf(fid, num2str(vector(n,m)));
    end
    fprintf(fid, '\n');
end
fclose(fid)
result = 'done';
end

