
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(d_k, 1)
 
    def forward(self, x1, x2, mask=None):
        attn = self.attn(x2).transpose(-1, -2).contiguous()  # Compute the dot product between the attention vectors for the two inputs
        attn = torch.sigmoid(attn)  # Apply sigmoid to the scaled attention vector
        if mask is not None:
            attn = attn.masked_fill(mask == 0, float("-inf"))  # Set the value of attention to -inf where the mask value is 1
        v1  = torch.einsum("bijcd,bcd->bici", x1, attn)  # Compute dot product between x1 and the scaled attention vector for the two inputs
        output = torch.einsum("bcidi,bcd->bcdjcd", attn, x2)  # Compute dot product between the dropout output of the scaled attention vectors for the two inputs
        return output


# Initializing the model
m = Model()

