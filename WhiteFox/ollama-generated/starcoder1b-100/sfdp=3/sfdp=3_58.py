
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(d_model, d_k)
        self.k = torch.nn.Linear(d_model, d_k)
        self.v = torch.nn.Linear(d_model, d_k)
 
    def forward(self, x):
        q = self.q(x)  # Compute the query tensor
        k = self.k(x)  # Compute the key tensor
        v = self.v(x)  # Compute the value tensor
        s = torch.matmul(q, k.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        t = torch.nn.functional.softmax(s / temperature, dim=-1)  # Apply softmax to the scaled dot product
        output = torch.matmul(t, v)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


