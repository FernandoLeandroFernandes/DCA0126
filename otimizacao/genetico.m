% Numero de individuos
num_ind = 30;

% Numero de geracoes
num_ind = 50;

ind = randi(2, num_ind, 16)-1;

% x1 => 8 bon 1:8
% x2 => 8 bon 9:16

adap_ind = zeros(num_ind, 1);

for i = 1:num_ind
	aux_1 = bi2de(ind(i, 1:8));
	aux_2 = bi2de(ind(i, 9:16));
	adap_ind(i) = fun(aux_1, aux_2);
end

% Melhor da populacao inicial
[max_adap, I_melhor] = max(adap_ind);

% Adaptacao relativa
adap_rel = adap_ind/sum(adap_ind);

% Selecao dos pais (roleta)
for i = 2:num_ger
	
	% Selecao dos pais
	for j = 1:10
		pais(i) = ind(roleta(adap_rel), :);
	end

	% Cruzamento 
	for j = i:2:(num_ind/2)-1
		flag = randi(7);
		a = randi(10);
		b = randi(10);
		filho(j,:)   = [pais(a, 1:flag, pais(b, flag+1:8)) pais(a, 9:flag+8, pais(b, flag+9:16))]
		filho(j+1,:) = [pais(b, 1:flag, pais(a, flag+1:8)) pais(b, 9:flag+8, pais(a, flag+9:16))]
	end

	% Mutacao
	% ...
end

function I = roleta(adapRel)
	bola = rand();
	for i = 1:length(adapRel)
		if bola <= sum(adapRel(1:i))
			I = i;
			break;
		end
	end
end

function z = fun(a, b)
	z = sin(a). * sin(b)./(a.*b);
end