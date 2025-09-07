
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = x1 .permute(0, 2, 1) # Permute tensor A with the shape of [batchsize, 3, 4]
        v2 = x2 .permute(0, 1, 2)# Permute tensor B with the shape of [batchsize, 5, 4]

        v3 = torch.bmm(v1, v2) # Compute the bmm between the permuted tensors A and B
        return self.linear(v3)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(64, 50 , 4).to(device=device) # Tensor A with shape [batchsize, 50, 4]
x2 = torch.randn(64, 3,  4).to(device=device)    # Tensor B with shape [batchsize, 3, 4]
