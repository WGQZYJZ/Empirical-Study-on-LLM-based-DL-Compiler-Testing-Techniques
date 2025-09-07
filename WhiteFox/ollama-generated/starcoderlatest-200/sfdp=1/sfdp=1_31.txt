
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Conv2d(1, 8, 3)
        self.k = torch.nn.Linear(4096, 8)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of two tensors (x1 and x2). Note that this requires specifying how to transpose both inputs with `transpose`.
        qk = self.q(qk) + self.k(x1.view(x1.size(0), 4096)).unsqueeze(-1).unsqueeze(-1) # Add the output of the linear layer (of dimension 4096 * 8, and broadcasted over batch size x2.size(0) * x1.size(0)) to the output of the convolution with kernel size 3
        qk = torch.softmax(qk, dim=-1) # Apply softmax on the final dimension (after broadcasting to batch size)
        qk = torch.nn.functional.dropout(qk, p=0.5) # Dropout is applied before the linear transformation. Here we apply dropout with probability 0.5 on the output of the attention mechanism (qk)
        qk = qk.matmul(x2) # Compute the dot product of the scaled dot product and the key tensor (x2)
        return qk

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(3, 8, 512, 512)
