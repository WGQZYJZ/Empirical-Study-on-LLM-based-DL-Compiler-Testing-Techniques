
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.randn((48, 3)) # Generate a random 3D tensor with the size of [48] and [3]
        v2_transversed  = v2.transpose(-2, -1) # Transpose this 3D tensor from [-2, -1] to [-1, -2]
        v5  = torch.randn(v2.size(-1), v2.size(-2)) # Generate a random 3D tensor with the size of [3] and [48]
        v7_mask  = torch.triu(torch.ones((v5.size()[:-1]), device=v5.device) * -float("inf")) + torch.diag(
            torch.tensor([0.], device=v2.device)) # Generate a triangular matrix from the [-3, -2] to [-1, 1], and add diagonal entries of [0].
        v8  = (v5 @ v2_transversed) / math.sqrt(torch.sum(v7_mask).to(dtype=torch.float64)) # Compute the dot product of the query and key tensors, then scale them by the square root of their size [-1]
        v9  = (v5 @ v2_transversed) + v7_mask # Add the attention mask to the scaled dot-product result
        v10  = torch.softmax(v8, dim=-1) # Apply softmax to the result
        v14  = x1.size(-1) * v5.size()[-1] - v9 # Subtracting the resulting tensor from the original size
        v23_masked  = F.dropout(v10, p=0.0768, training=self.training) @ (x1 + v14).transpose(-2,-1) # Apply dropout to the softmax output with a probability of 0.95
        return torch.cat([F.adaptive_avg_pool3d(v23_masked, (torch.tensor(7), x1.size()[-2], x1.size()[-3]), 4.0), F.adaptive_max_pool3d(
            v23_masked, 8.0)], dim=1)


# Initializing the model