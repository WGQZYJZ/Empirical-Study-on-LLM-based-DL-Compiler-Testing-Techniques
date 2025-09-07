
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_conv = torch.nn.Conv2d(3, 16, 5, stride=2, padding=2)
        self.k_conv = torch.nn.Conv2d(3, 8, 5, stride=2, padding=2)
 
    def forward(self, x1, x2):
        q = self.q_conv(x1)
        k = self.k_conv(x2)
 
        v1 = self.q_conv(x1)
        v2 = v1 * 0.5
 
        scaled_qk = torch.matmul(q, k.transpose(-2, -1)) # Compute the dot product of the query and the key
        softmax_qk = scaled_qk / (0.001 + scaled_qk.abs().sum(-1).view(scaled_qk.shape[0], -1).pow(2).sum(-1).view(scaled_qk.shape[0], -1).sqrt()) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = (1 + scaled_qk.detach()).matmul(dropout_qk).matmul(v2)
 
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 32, 32)
