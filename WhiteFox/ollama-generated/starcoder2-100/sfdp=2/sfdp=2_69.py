
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(784, 512)
        self.key = torch.nn.Linear(784, 512)
        self.value = torch.nn.Linear(784, 512)
 
    def forward(self, x):
        vq = F.relu(self.query(x))
        vk = F.relu(self.key(x)) 
        vv = F.relu(self.value(x)) 
        inv_scale_factor = torch.tensor([0.01827])  # Compute the inverse scale factor to scale the dot product of the query and key by
        scaled_qk = qk.div(inv_scale_factor) 
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.2)  
        output  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(64, 784)
__output__  = m(x1)

