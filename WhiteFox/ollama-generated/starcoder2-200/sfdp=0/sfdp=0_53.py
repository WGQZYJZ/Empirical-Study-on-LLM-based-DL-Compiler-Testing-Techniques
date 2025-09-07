
import torch
from torch import nn

class MultiHeadAttention(nn.Module):

    def __init__(self):
        super().__init__()

        # The number of heads determines how many different weight matrices are used to compute the dot product in the scaled self-attention mechanism. 
        # In practice, a larger number of heads gives better performance, although at a higher computational cost.
        self.head_dim = 8
        self.d_model = 256

        # The d_k parameter is used when scaling to prevent explosion during the softmax operation in scaled dot-product attention. 
        # In practice it may be necessary to experiment with different values depending on your application and data.
        self.d_k = int(self.d_model / self.head_dim)

        # Embedding layers used for the MultiHeadAttention mechanism. The embedding weights are initialized randomly and the input dropout is enabled during training. 
        self.query_embedding, self.key_embedding, self.value_embedding = nn.ModuleList([
            nn.Linear(self.d_model, self.head_dim * self.d_k),
            nn.Linear(self.d_model, self.head_dim * self.d_k)
        ]), \
           nn.ModuleList([
               nn.Linear(self.d_model, self.head_dim * self.d_k),
               nn.Linear(self.d_model, self.head_dim * self.d_k)
           ]), \
           nn.ModuleList([
            # The output dropout is used to regularize the outputs of the MultiHeadAttention mechanism and reduce overfitting during training. It may not be necessary in your case.
            nn.Dropout(0.1), 
            nn.Linear(self.head_dim * self.d_k, 8)
        ])

        # The scaled dot product attention layer used for the MultiHeadAttention mechanism is initialized with an embedding dropout probability of 0.3 and scaled to prevent numerical overflow issues during the softmax operation.
        # This allows the model to train more efficiently when the embedding dimension d_model is large. 
        self.attention = nn.MultiheadAttention(self.d_k, dropout=0.3)

    def forward(self, queries):

        # The query input for this MultiHeadAttention layer should have dimensions: [batch size, number of queries in each sequence, embedding dimension].
        # In this case it would be 64, which means that there are 64 sequences per batch containing 10 inputs.
        # The embedding dimension here is 256.
        batch_size = queries.shape[0]
        query_input = self.query_embedding(queries).view(-1, batch_size * 10, self.d_model)

        # Similarly for the key and value inputs, the batch size is also equal to 64 but number of keys in each sequence is not equal to 10. 
        # In this case it would be 28. The embedding dimension here is 256 too.
        # Therefore, we reshape the key input before passing through a linear layer and concatenate with the value inputs.
        key_input = self.key_embedding(queries).view(-1, batch_size * 28, self.d_model)

        # The value inputs for this MultiHeadAttention layer should have dimensions: [batch size, number of keys in each sequence, embedding dimension]. 
        # In this case it would be 28, which means that there are 28 sequences per batch containing 10 keys and 3 values.
        # The embedding dimension here is 256.
        
        value_input = self.value_embedding(queries).view(-1, batch_size * 28, self.d_model)

        # Now we finally pass these three inputs into the scaled dot-product attention layer to compute the output features. 
        # The attention weights are computed by dividing the input embeddings by the square root of their d_k value and passing them through a softmax function.
        # This prevents numerical overflow issues during the softmax operation.
        
        query, key = torch.chunk(query_input, chunks=2)
        value, scale = self.attention(key, query)[0], key

        # The resulting output features are then passed to one more linear layer, followed by a ReLU nonlinearity and dropout. 
        # This is used to regularize the model's output features in the MultiHeadAttention mechanism.
        
        attention_output = nn.functional.relu(
            self.key_embedding[0](scale) + \
            self.query_embedding[1](self.value_embedding[1](self.attention(query, value)[0]))
        )

        return self.value_embedding[-1](nn.Dropout(0.3)(self.value_embedding(-1)(attention_output)))


