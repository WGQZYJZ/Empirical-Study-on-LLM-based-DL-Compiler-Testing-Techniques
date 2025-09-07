
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(...) # Permute the input tensor A
        v2 = input_tensor_B.permute(...) # Permute the input tensor B

        w1 = input_tensor_A.unsqueeze(-1)  # Unsqueeze the second to last dimension of tensor A.
        w2 = torch.matmul(input_tensor_B, t2) # or torch.bmm(t1, t2)

        v3 = torch.tanh(torch.add(w1, w2)) # Or: torch.nn.functional.linear(w1, ...) + torch.nn.functional.linear(w2, ...)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(...)
x2 = torch.randn(...)
