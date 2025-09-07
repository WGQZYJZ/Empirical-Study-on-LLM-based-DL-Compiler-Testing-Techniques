
class SelfAttention(torch.nn.Module):
    def __init__(self, d_model, nheads=128, dropout = 0.1):
        super().__init__()

        self.scale = math.sqrt(d_model)

        # Create a multi-head attention layer which is a combination of the input embedding, position embeddings and scaled dot product attention. 
        # This combination can improve efficiency when computing multiple independent subqueries in parallel.
        self.self_attention_layer = torch.nn.MultiheadAttention(nheads=nheads, embed_dim=d_model)
 
        # Add a dropout layer after the multi-head attention layer to avoid overfitting.
        self.dropout = torch.nn.Dropout(p=dropout)
 
    def forward(self, q1):
        # Pass input embedding and position embeddings through linear layers with batch norm and activation functions for better results
        x1 = q1 * self.scale
 
        # Pass the output of linear layer through multi-head attention layers which compute the weights and outputs in the query tensor
        v1, _ = self.self_attention_layer(x1, x1, x1)
 
        # Apply dropout after the attention computation to avoid overfitting
        v2 = self.dropout(v1)
        
        # Return a tensor of output with shape [bs, q1.shape[0], d_model]
        return v2
 
    def init_weights(self): 
        