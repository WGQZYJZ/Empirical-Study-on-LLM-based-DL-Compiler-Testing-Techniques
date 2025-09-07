
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.dot(x2, x3) / math.sqrt(x4.size(-1)) + self._attn_mask  # Compute the dot product of the query and key tensors
        v2  = torch.softmax(v1, dim=-1)
        v3  = v2 @ v5
        return v6

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1024, 768, device='cuda')  # A tensor with shape (batch_size=1, embedding_dimension=768) that is used as the query tensor in scaled dot product attention
x2 = torch.randn(512, 768).to('cuda')  # A randomly generated tensor of shape (query_tensor_dimension=512, key_value_dimension=768), which is used as the key tensor in scaled dot product attention
x3 = x2.transpose(-2,-1)  # Transpose the input tensors to make them compatible with PyTorch's softmax function. The -1 argument refers to the last dimension of the input, and the -2 argument refers to a second-to-last dimension.
x4 = torch.randn(768).to('cuda')  # A randomly generated tensor with shape (value_dimension=768) that is used as the value tensor in scaled dot product attention

