
class TransformerEncoderBlock(torch.nn.Module):
    def __init__(self, config: dict) -> None:
        super().__init__()
        self.embedding = torch.nn.Embedding(
            num_embeddings=config["embed_dim"], embedding_dim=config["embed_dim"]
        )
 
        self.encoder1 = nn.Linear(in_features=config["embed_dim"], out_features=2048) 
        self.encoder2 = nn.Linear(in_features=2048, out_features=256)

        self.norm1 = torch.nn.LayerNorm(normalized_shape=[-1], eps=1e-13)
        self.norm2 = torch.nn.LayerNorm(normalized_shape=[-1], eps=1e-13)
 
    def forward(self, inputs):
        input_seq = self.embedding(inputs)
 
        residual = input_seq
        output = self.encoder1(residual)
        output = self.encoder2(output)
        output = self.norm1(input_seq + output)
 
        residual = output
        output = torch.nn.LeakyReLU()(output)
        output = self.norm2(residual + output)
        return output
 
class TransformerDecoderBlock(torch.nn.Module):
    def __init__(self, config: dict) -> None:
        super().__init__()
        self.embedding1 = torch.nn.Linear(in_features=config["embed_dim"], out_features=2048) 
        self.embedding2 = torch.nn.Embedding(
            num_embeddings=config["embed_dim"], embedding_dim=config["embed_dim"]
        )

        self.encoder1 = nn.Linear(in_features=config["embed_dim"], out_features=2048) 
        self.encoder2 = nn.Linear(in_features=2048, out_features=256)
 
        self.norm1 = torch.nn.LayerNorm(normalized_shape=[-1], eps=1e-13)
        self.norm2 = torch.nn.LayerNorm(normalized_shape=[-1], eps=1e-13)
 
    def forward(self, inputs):
        residual = inputs
        output = self.embedding1(residual)
        output = self.encoder1(output) 
        output = self.encoder2(output)
 
        residual = output
        output = torch.nn.LeakyReLU()(input_seq + output)
        
        output = self.norm1(residual + output)
 
        residual = output
        output = self.embedding2(residual)
        output = self.norm2(residual + output) 
        return output
 
class TransformerDecoder(torch.nn.Module):
    def __init__(self, config: dict) -> None:
        super().__init__()
        self._transformer_decoder_blocks = nn.Sequential()
 
        for i in range(config["num_layers"] - 1):
            self._transformer_decoder_blocks.add_module(f"layer_{i}", TransformerDecoderBlock(config))
 
    def forward(self, inputs) -> torch.Tensor:
        return self._transformer_decoder_blocks(inputs)

