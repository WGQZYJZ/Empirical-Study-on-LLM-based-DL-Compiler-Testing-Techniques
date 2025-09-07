
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        qk = torch.matmul(x2, x1.transpose(-2, -1)) # Compute the dot product of the query and the key
        inv_scale_factor = torch.rsqrt((torch.pow(v2, 2) * torch.pow(qk, 2) + eps).clamp(min=eps).reciprocal()) # Compute the inverse scale factor
        softmax_qk = qk / (inv_scale_factor * torch.pow(v2, 0.5)) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value


# Initializing the model
m  = Model()


