clear all
close all
%%
N = 512;
M = 128;
K = 8;
T=100;
a = (randn(N,1)+randn(N,1)*1j)/sqrt(2);
mask_index = randperm(N,K);
mask = zeros(N,1);
mask(mask_index) = 1;
h = a.*mask;
A = (randn(M,N)+randn(M,N)*1j)/sqrt(2);
A = A/sqrt(M);
[U,S,V] = svd(A); %A = U*S*V'.
S_iden = eye(M,N);
A_iden = U*S_iden*V';
y = A*h;
y_procedure = zeros(M,T);
hhat = A'*A*h;
figure
stem(abs(h),'LineWidth',2,'MarkerSize',10,'marker','diamond')
hold on
stem(abs(hhat),'LineWidth',1.5)
axis([1 N 0 2])
grid on