
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_module = torch.nn.Linear(64, 64)
 
    def forward(self, qk, vq):
        v6 = self.attn_module(vq).reshape(vq.shape[0], 1, -1) * qk # Apply a pointwise multiplication of the value and the query to compute attention
        softmax_v6 = torch.nn.functional.softmax(v6, dim=-2) # Apply softmax to v6 to obtain probabilities of how much it should be multiplied by the key tensor
        output = (qk * softmax_v6).transpose(-2, -1).matmul(vq)  # Compute the dot product of qk and softmaxed vq and then apply a linear transformation on both sides of the multiplication to get outputs for each head in a multi-head attention model 
        return output


# Initializing the model
m = Model()

# Query to the model
qk = torch.randn(1, 64, 5, 3)
vq = torch.randn(1, 64, 64, 64)
