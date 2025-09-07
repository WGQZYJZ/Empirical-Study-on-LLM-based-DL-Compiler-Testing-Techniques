
class TransformerModel(torch.nn.Module):
    def __init__(self, d_model: int = 512, num_heads: int = 8):
        super().__init__()
 
        self.attention_layer_1 = torch.nn.MultiheadAttention(d_model, num_heads) 
        # Apply the multihead attention layer to two inputs of shape (B, N, C), and return outputs of shape (B, N, H*W*C).
        # The parameters of the multi-head attention module are defined in nn.MultiheadAttention, which takes a single integer argument, num_heads.
 
        self.attention_layer_2 = torch.nn.Linear(d_model, d_model)
        # Apply an MLP to output the scaled dot product between all heads (i.e., input tensor and outputs of attention layer 1),
        # which returns a vector of shape (B, N, C). 
        # The parameters of this linear layer are defined in nn.Linear, which takes two integers arguments: d_model and num_classes.
 
        self.linear_layer = torch.nn.Linear(d_model, d_model)
        # Apply an MLP to output the scaled dot product between all heads (i.e., input tensor and outputs of attention layer 2), 
        # which returns a vector of shape (B, N, C). The parameters of this linear layer are defined in nn.Linear, 
        # which takes two integers arguments: d_model and num_classes.
 
    def forward(self, x):
        x1 = self.attention_layer_1(x, x, x)[0]  # attention_weights_linear will return a vector of shape (B, N, C) after applying the linear layer to the outputs of attention_layer_1 and the outputs of attention_layer_2.
 
        x2 = self.attention_layer_2(x1).transpose(-1, -2) # scaled_dot_product will return a matrix of shape (B, N, H*W) after applying the linear layer to the output of linear_layer and all heads in attention_weights_linear.
 
        x3 = self.linear_layer(x2)  # attention_context will be returned
        return x3


# Initializing the model
m = TransformerModel()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
