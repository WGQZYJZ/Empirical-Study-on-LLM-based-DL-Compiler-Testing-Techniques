
import torch
class Model(torch.nn.Module):
    def __init__(self, hidden=64, nheads=8, input1d = 50):
        super().__init__()
        self.input1d = input1d
 
        self.pos_enc1 = torch.nn.Parameter(torch.randn(2*input1d, hidden)) # Create a parameter of shape (2*input1d x hidden) with random values
        self.pos_enc2 = torch.nn.Parameter(torch.zeros(hidden, input1d)) # Create another parameter of shape (hidden x 50), filled with zeros
 
        self.norm = torch.nn.LayerNorm(hidden) # Apply the LayerNorm operation to hidden
        self.attn = torch.nn.MultiheadAttention(hidden=hidden, num_heads=nheads)
 
    def forward(self, x):
        t1 = torch.matmul(x + self.pos_enc1[: , None], 
                          (torch.exp(-2*math.pi*(None if torch.__version__<"1.7" else 0.5)*torch.arange(len(self.input1d))[None,:]))).transpose(-3,-4) # Apply the error function to the result
        t2 = self.norm(x) # Apply LayerNorm to x
        t3 = self.attn(t1,t2)[0] + 1 # Add 1 to the output of the attention mechanism
        return None

x  = torch.zeros([64,input1d])
out_tensor  = m(x)

