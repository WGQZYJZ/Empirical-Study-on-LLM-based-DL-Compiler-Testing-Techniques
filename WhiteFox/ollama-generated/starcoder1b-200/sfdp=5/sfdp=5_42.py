
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.1, attn_dropout_p=0.3):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout_p)
        self.attn = Attention()

    def forward(self, x1, x2):
        # x1 and x2 are of shape [B, C, H, W]
        output  = x1 @ x2 # Dot product of the two input tensors is the output of the convolution
        output += self.attn(x1, x2) # Add attention weights to the dot product result
        output = self.dropout(output) # Apply dropout to the dot product result
        return output


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(2, 3, 64, 64)
x2  = torch.randn(2, 8, 64, 64)
