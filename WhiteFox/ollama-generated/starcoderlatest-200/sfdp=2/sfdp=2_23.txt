
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(8 * 64, 16)
        self.linear = torch.nn.Linear(16, 64)
 
    def forward(self, x1, x2):
        v1 = x1 * 0.5 # Multiplies the output of layer x1 by 0.5
        v2 = x2 * 0.7071067811865476 # Multiplies the output of layer x2 by 0.7071067811865476
        qk = torch.matmul(v1, v2.transpose(-2, -1)) # Computes the dot product of two tensors
        scaled_qk = qk / np.sqrt(v1.shape[-1]) # Scales the dot product by 1/sqrt(dim) (i.e., the square root of the number of features in each vector in the input tensor)
        softmax_qk = scaled_qk.softmax(dim=-1) # Applies softmax to the scaled dot product
        output = self.attention(softmax_qk) # Multiplies a matrix with itself element-wise 
        return output + x2 # Addition


# Initializing the model
m = AttentionModel()

