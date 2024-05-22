return {
    "stevearc/conform.nvim",
    opts = {
        formatters_by_ft = {
            lua = { "stylua" },
            bash = { "shellhardern", "shfmt" },
            python = { "isort", "black", "ruff_fix", "ruff_format"},

        },
    }
}
