class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.permute(x1, 0, 2, 1) # Permute tensor A
        v2 = input_tensor_B.permute(...) # Permute tensor B
        v3 = torch.matmul(v1, v2) 
        return v3
