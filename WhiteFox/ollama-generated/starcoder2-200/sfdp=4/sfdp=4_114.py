class SelfAttentionBlock(torch.nn.Module):
    def __init__(self, d_model: int = 640) -> None:
        super().__init__()

        self._query_projection = torch.nn.Linear(
            in_features=d_model, out_features=256, bias=False
        )

    def forward(
        self, query: torch.Tensor
    ) -> Tuple[torch.Tensor]:  # type: ignore

        return (
            self._query_projection(query) @ torch.triu(
                torch.ones([3074, 3074]), diagonal=1
            ).to(torch.bool)
        )


self_attn = SelfAttentionBlock()
