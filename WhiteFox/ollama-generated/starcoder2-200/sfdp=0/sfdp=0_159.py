
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor) -> Tuple[Tensor]:
        # compute the scaled dot product of `query` and `key` using their transpose.
        # The dimensionality of these tensors will be `batch_size`, `sequence_length`, `d_model`.
        # You can call `torch.bmm` for matrix multiplication between 3D matrices, 
        # or use `torch.matmul(x1, x2)` to compute the dot product of two 2D matrices
        scaled_dot_product = torch.matmul(query, key.transpose(-2,-1)) / sqrt(query.size[-1])
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = torch.matmul(attention_weights, value)
 
        return (output,)

class MultiHeadAttentionLayer(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor, mask: Optional[Tensor] = None) -> Tuple[Tensor]:

        # compute the scaled dot product of `query` and `key` using their transpose. 
        # The dimensionality of these tensors will be `batch_size`, `sequence_length`, `d_model`.
        # You can call `torch.bmm` for matrix multiplication between 3D matrices, or use
        # `torch.matmul(x1, x2)` to compute the dot product of two 2D matrices. 
        scaled_dot_product = torch.matmul(query, key.transpose(-2,-1)) / sqrt(query.size[-1])
 
        if mask is not None:
            # apply mask to attention_weights by using `masked_fill` method on the output of the scaled dot product
            # mask should be a boolean 3D tensor with 0 and 1 values. 
            # You can call `torch.masked_fill(input, mask, value)` for this operation
            attention_weights = scaled_dot_product.masked_fill_(mask == 0., float("-inf"))
 
        # use the scaled dot product to compute the weights used in performing a weighted sum 
        # over the values from the original tensors
        attention_weights = attention_weights.softmax(dim=-1)
 
        output = torch.matmul(attention_weights, value)

        return (output,)

class Transformer(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor, mask=None, dropout=0.) -> Tuple[Tensor]:

        # add a positional encoding to the input. 
        # The positional encoding vector should be of size `sequence_length` and has a 3D dimensionality.
        # To implement this operation, you can call `torch.einsum` method in PyTorch or use `tensor.size(0)` method from a 1-D tensor to get batch size of the input tensors.

        sequence_length = query.size(-2)
 
        positional_encoding = torch.empty([sequence_length + 1, 3, dmodel], dtype=torch.float32).to(query.device)
        positional_encoding[:, 0] = torch.ones((sequence_length + 1,), dtype=torch.float32).to(query.device) * positional_encoding[:, 0].new_full((dmodel,), 1.)
        # set the position of 1st dimension to 1 in the positional encoding vector
 
        for i in range(1, sequence_length + 1):
            positional_encoding[i] = torch.einsum("i, j->ij", [i, torch.arange(-sequence_length // 2, sequence_length // 2).to(positional_encoding)], [1., 0.5])
 
        positional_encoding = torch.nn.functional.normalize(positional_encoding)
        query += positional_encoding[1:].clone().detach()
        key += positional_encoding.clone().detach()

        # call the scaled dot product attention method to compute the output of the MultiHeadAttentionLayer object using query, key and value tensors as input arguments. 
        # In addition, set `mask` argument equal to the 3D mask variable used in the previous example
        # call the `torch.nn.Dropout` method on the output of the scaled dot product attention layer to apply dropout

        masked_scaled_dot = ScaledDotProductAttention()
        output1 = masked_scaled_dot(query=query, key=key, value=value)
        output2 = torch.nn.functional.dropout(output1[0], p=dropout)
 
        # call the scaled dot product attention method to compute the output of the MultiHeadAttentionLayer object using query, key and value tensors as input arguments.
        # In addition, set `mask` argument equal to None
        # call the `torch.nn.Dropout` method on the output of the scaled dot product attention layer to apply dropout

        masked_scaled_dot = ScaledDotProductAttention()
        output1 = masked_scaled_dot(query=query, key=key, value=value)
        output3 = torch.nn.functional.dropout(output1[0], p=dropout)
 
        return (output2 + output3,)
