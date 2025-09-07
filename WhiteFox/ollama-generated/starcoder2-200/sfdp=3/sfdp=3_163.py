
class Model(torch.nn.Module):
    def __init__(self, d):
        super().__init__()
        self.dropout  = torch.nn.Dropout(p=0.1)
        self.scale    = 1 / math.sqrt(d)
 
    def forward(self, qk_tensor, value_tensor):
        dot_product  = torch.matmul(qk_tensor, value_tensor.transpose(-2, -1))
        scaled_dot   = dot_product * self.scale
        sofmaxed     = scaled_dot.softmax(dim=-1)
        softmaxed    = dropout(sofmaxed, p=0.5, train=True) # train=True to generate the model with a random state
        output       = softmaxed @ value_tensor  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model