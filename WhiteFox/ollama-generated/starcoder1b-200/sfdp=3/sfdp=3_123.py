
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(d_model, d_k)  # Compute the linear projection matrix for query and key tensors
        self.o = torch.nn.Linear(d_k, o_dim)  # Compute the linear projection matrix for output of attention mechanism

    def forward(self, x1, x2):
        v1 = self.qkv(x1).contiguous()  # Unpack query and key tensor
        v2 = self.o(v1)  # Project to output projection matrix
        v3 = torch.cat((x1, x2), dim=-1)  # Concatenate input and attention mechanism output to form new input tensor
        return v3


# Initializing the model
m = Model()


