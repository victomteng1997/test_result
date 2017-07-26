% run the coeff before start analyzing
vectors = [b,a];
vectors = to_binary(vectors,16);
write_binary_into_txt(vectors);  % deviation of group delay is in a form of which num dev first then followed by den dev
[gd,w] = grpdelay(b,a,314);
tau = 10;           %need to be modified for each experiment
matrix = zeros(length(gd),1);
matrix(:,:) = tau;
etau =  gd - matrix;
disp('inital etau')
disp(norm(etau(1:round(0.4*314)),inf))
max_index = find(etau==(max(etau)));
min_index = find(etau==(min(etau)));
gradient = Gra_Dev_Group_delay(b,a,314,gd,tau);
s_map = get_smap(gradient,max_index,min_index);