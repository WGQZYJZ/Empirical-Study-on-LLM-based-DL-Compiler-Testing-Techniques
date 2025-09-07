
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Conv2d(8, 32, kernel_size=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) # compute the dot product of two tensors
        scaled_qk = qk / 0.70710678118654759375 ** (1/2) # scale by 1/(0.707^0.5) for each element in the dot-product matrix
        softmax_qk = scaled_qk.softmax(dim=-1) # apply softmax to each row of the dot-product matrix, so that the result contains attention scores for every position and every head 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5) # apply dropout with probability 0.5
        output = dropout_qk @ x2 # compute attention score
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16, 8, 32, 32)
x2 = torch.randn(16, 32, 32, 32)
