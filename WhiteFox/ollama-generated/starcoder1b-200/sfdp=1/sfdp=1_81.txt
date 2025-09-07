
class Model(torch.nn.Module):
    def __init__(self, embedding_dim=512, num_heads=8):
        super().__init__()

        self.embedding = torch.nn.EmbeddingBag(num_embeddings=4000,
                                               embedding_dim=embedding_dim,
                                               max_norm=None,
                                               norm_type=2,
                                               padding_idx=None)

        self.transformer_ffn = TransformerFFN(
            d_model=1024,
            num_attention_heads=num_heads)

    def forward(self, inputs):
        embeddings = self.embedding(inputs)
        x = torch.matmul(embeddings, self.transformer_ffn.proj_layer)
        return F.log_softmax(x, dim=-1)


# Initializing the model
m = Model()


