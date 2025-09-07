
class Model(torch.nn.Module):
    def __init__(self, query_shape: torch.Size, key_shape: torch.Size, value_shape: torch.Size,
        query_projection_dim: int = 32, key_projection_dim: int = 64, value_projection_dim: int = 32):
        super().__init__()
        # The shape of the projection layer that projects the input tensor to a dimension for the attention matrix multiplication
        self.query_projection = torch.nn.Linear(
            in_features=query_shape[-1] if len(query_shape) == 4 else query_shape[0],
            out_features=query_projection_dim,
        )
 
        # The shape of the projection layer that projects the key tensor to a dimension for the attention matrix multiplication
        self.key_projection = torch.nn.Linear(
            in_features=key_shape[-1] if len(key_shape) == 4 else key_shape[0],
            out_features=key_projection_dim,
        )
 
        # The shape of the projection layer that projects the value tensor to a dimension for the attention matrix multiplication
        self.value_projection = torch.nn.Linear(
            in_features=value_shape[-1] if len(value_shape) == 4 else value_shape[0],
            out_features=value_projection_dim,
        )
 
        # The shape of the convolution layer that projects the output of the attention matrix multiplication by a constant factor to produce an attention score
        self.attention = torch.nn.Conv2d(
            in_channels=query_projection_dim + key_projection_dim + value_projection_dim,
            out_channels=32,
            kernel_size=(1, 1),
            stride=1,
            padding=0,
        )
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        # The following is a typical pattern for the computation of an attention matrix
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
 
        # The following is a typical pattern for the computation of an attention matrix from an embedding projection layer instead of a convolutional layer
        qk2 = torch.matmul(self.query_projection(query), self.key_projection(key).transpose(-1, -2))  # Compute the dot product of the query and key tensors
        scaled_qk2 = qk2.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk2 = scaled_qk2.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk2 = torch.nn.functional.dropout(softmax_qk2, p=dropout_p)  # Apply dropout to the softmax output
        output2 = dropout_qk2.matmul(self.value_projection(value))  # Compute the dot product of the dropout output and the value tensor
 
        attention_scores = torch.cat((qk, qk2), dim=-1)  # Concatenate the values for both tensors
        attention_scores = self.attention(attention_scores)  # Apply convolutional layer to the concatenation of the two inputs
        attention_weights = torch.nn.functional.softmax(attention_scores, dim=1).div(attention_scores.size(-1))  # Normalize by the size of the feature dimension
        attention_output = (attention_weights * value).sum(dim=-2)  # Dot-multiply the output with the scaled weights to produce an attention vector
        return attention_output


# Initializing the model
m = Model()


# Query, key, and value tensor inputs to the model
x1 = torch.randn(batch_size, input_feature_dimension)
__output1__ = m(x1, x2, x3)


class Model(torch.nn.Module):
    def __init__(self, query_shape: torch.Size, key_shape: torch.Size, value_shape: torch.Size,
        input_feature_dimension: int, hidden_dim: int = 64, output_dim: int = 32):
        super().__init__()
        # The shape of the embedding layer that projects the query tensor to a dimension for the attention matrix multiplication
        self.query_embedding = torch.nn.Embedding(
            num_embeddings=query_shape[0] if len(key_shape) == 1 else key_shape[-2],
            embedding_dim=hidden_dim,
        )
 
        # The shape of the embedding layer that projects the key tensor to a dimension for the attention matrix multiplication
        self.key_embedding = torch.nn.Embedding(
            num_embeddings=key_shape[0] if len(key_shape) == 1 else key_shape[-2],
            embedding_dim=hidden_dim,
        )
 
        # The shape of the convolution layer that projects the output of the attention matrix multiplication with aka, in case when we have a very long long long lame what. I think the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the the