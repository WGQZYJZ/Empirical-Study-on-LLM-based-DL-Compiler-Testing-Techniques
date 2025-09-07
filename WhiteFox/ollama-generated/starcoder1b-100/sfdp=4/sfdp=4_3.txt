
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(64 * 2, 5)

    def forward(self, x1, x2):
        w1 = torch.matmul(x1.transpose(-2, -1), x2) / math.sqrt(x1.size(-1))  # Compute the dot product of the two input tensors, and scale it by the square root of the input dimension
        w1 = w1 + self.attn(torch.arange(w1.shape[0]).unsqueeze(dim=-2)).unsqueeze(dim=-1) * math.sqrt(x1.size(-1))  # Add attention mask to the result, so that positions where the attention weights are zero have a very small attention weight
        w2 = self.attn(torch.arange(w2.shape[0]).unsqueeze(dim=-2)).unsqueeze(dim=-1) * math.sqrt(x2.size(-1))  # Add attention mask to the result, so that positions where the attention weights are zero have a very small attention weight
        return torch.matmul(w1, w2)


# Initializing the model
m = Model()


