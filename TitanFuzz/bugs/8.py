import torch
torch.manual_seed(420)
torch.cuda.manual_seed_all(420)
A = torch.rand(50, 50)
B = torch.clone(A).cuda()
C = torch.clone(A)
torch.mm(C, C, out=C)
print("cpu in place:", C)  # CPU (in place) gives wrong results
D = torch.mm(A, A)
print("cpu:", D)
print(torch.allclose(C, D)) # False

torch.mm(B, B, out=B)
print("GPU in place:", B)  # GPU gives right answer
print(torch.allclose(B.cpu(), D)) # True