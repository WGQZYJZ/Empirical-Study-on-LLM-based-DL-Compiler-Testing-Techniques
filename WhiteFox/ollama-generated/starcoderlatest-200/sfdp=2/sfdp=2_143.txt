
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        # Use this code snippet to generate the `attention_mask` tensor that applies dropout (i.e., with probability `dropout_p`) on each position of an input sequence:
        attention_mask = torch.ones(input_tensor.shape, device=input_tensor.device)
        attention_mask = torch.where(
            attention_mask == 1,
            torch.nn.functional.softmax(torch.rand(attention_mask.shape), dim=-1).to(attention_mask),
            attention_mask,
        )
        self.attn = torch.nn.Linear(key_vector.shape[-1], value_vector.shape[0])
 
    def forward(self, x):
        v  = torch.tanh(torch.matmul(x, self.attn)) # Apply tanh to the input tensor and then compute the dot product with the attention matrix
        return attention_mask * v


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(256, 3, 64, 64)
