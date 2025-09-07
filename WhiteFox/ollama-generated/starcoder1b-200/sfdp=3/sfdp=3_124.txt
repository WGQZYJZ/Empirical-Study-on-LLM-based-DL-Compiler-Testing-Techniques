
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(512, 8)
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk  = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk  = qk.mul(scale_factor)  # Scale the dot product by a factor
        dropout_qk = torch.nn.functional.dropout(scaled_qk.softmax(dim=-1), p=dropout_p)  # Apply dropout to the softmax output
        v = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        attn  = self.attn(x2)  # Compute the attention weights of x2 (output from conv layer)
        return attn * v


# Initializing the model
m = Model()


