% Otimizacao enxame de particulas

%Parametros iniciais
w = 1.25;
phi1 = 1.4;
phi2 = 1.4;

% Numero de particulas do enxame inicial
num_part = 30;

% Numero de enxames inicial
num_enx = 50;

max_xy = 100;
min_xy = -100;

% Vetor posicao
x = min_xy + (max_xy - min_xy)*rand(num_part, 2);

% Vetor velocidade
v = zeros(num_part, 2);

for i = 1:num_part
	z(i,:) = fitness(x(i,1), x(i,2));
end

% Pbest inicial
pbest = x;
zpbest = z;

% Gbest inicial
[zgbest, I] = max(z);
gbest = x(I,:);

for j = 2:num_enx
	for i = 1:num_part
		v(i,:) = w*v(i,:) + rand()*phi1*(pbest(i)-x(i:)) + rand()*phi2*(gbest-x(i,:));
		x(i,:) = x(i,:) + v(i,:);
		z(i,:) = fitness(x(i,1)),x(i,2);

		% Atualizar o pbest
		if (zpbest < z(i))
			pbest(i,:) = x(i,:);
			zpbest = z(i);
		end

		% Atualizar o gbest
		if (zgbest < zpbest)
			gbest = pbest(i,:);
			zgbest = zpbest(i);
		end
	end
end 

function z = fitness(x1, x2)
	z = sin(x1)*sin(x2)/(x1*x2);
end