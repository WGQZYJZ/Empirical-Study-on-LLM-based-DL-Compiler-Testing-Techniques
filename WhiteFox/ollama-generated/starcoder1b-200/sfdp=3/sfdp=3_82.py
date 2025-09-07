
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_layer = torch.nn.Linear(10, 4)
        self.key_layer = torch.nn.Linear(128, 4)
        self.value_layer = torch.nn.Linear(128, 4)
 
    def forward(self, x1):
        vq  = torch.matmul(x1, self.query_layer(x1))  # Compute the dot product of the query and key tensors
        vk  = torch.matmul(x1, self.key_layer(x1))  # Compute the dot product of the query and key tensors
        vq  = vk.mul(0.5)  # Scale the dot product by a factor
        sk  = torch.exp(vk - 0.2 * torch.log(torch.abs(vk + 1e-9)))
        dv  = torch.matmul(x1, self.value_layer(x1))  # Compute the dot product of the query and key tensors
        output  = sk.mul(dv)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


