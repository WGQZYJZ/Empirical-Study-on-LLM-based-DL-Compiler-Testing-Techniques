
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_conv = torch.nn.Conv2d(3, 16, 7, stride=1, padding=0)
        self.k_conv = torch.nn.Conv2d(8, 16, 5, stride=1, padding=4)
        self.v_conv = torch.nn.Conv2d(8, 16, 3, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk  = torch.matmul(self.q_conv(x1), self.k_conv(x2).transpose(-2,-1)) # Apply convolutions to produce query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.v_conv(x2)) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
