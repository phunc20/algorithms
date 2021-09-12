### A Pluto.jl notebook ###
# v0.15.1

using Markdown
using InteractiveUtils

# ╔═╡ 882c47a6-13c5-11ec-2eee-5f38073a3824
begin
  using TikzPictures
  using LaTeXStrings
end

# ╔═╡ 0391208b-b2ab-4240-a681-37bc7ded21ab
let
	a = "A"
	"ab$(a)"
end

# ╔═╡ 52dfc51b-bcc7-44ed-93f3-5a616cb7ac5d
let
  TikzPicture(
    L"""
    \def\fillcolor{gray}
    \def\radius{3ex}
    \def\height{4.5ex};
    \draw[fill=\fillcolor,\fillcolor] (2*\radius, 0) circle (\radius);
    \node[\fillcolor] at (6*\radius, 0) {\Huge $\cdots$};
    \draw[fill=\fillcolor,\fillcolor] (10*\radius, 0) circle (\radius);
    """,
    #options="scale=1.5",
    preamble="")
end

# ╔═╡ 9734ee4b-1a80-4de0-8293-cfd7817663b6
let
  TikzPicture(
    L"""
    \def\fillcolor{gray}
    \def\radius{2ex}
    \def\height{4.5ex}
    \node (left parent) at (5*\radius, 0) [circle, draw=gray, fill=gray, inner sep=\radius] {};
    \node [white, above] at (left parent.north) {\large $2^{n}$};
    \node (right parent) at (10*\radius, 0) [circle, draw=gray, fill=gray, inner sep=\radius] {};
    \node[\fillcolor] at (6*\radius, 0) {\Huge $\cdots$};
    """,
    #options="scale=1",
    preamble="")
end

# ╔═╡ 06e834ff-8904-46a6-b554-014ca15541c9
let
  TikzPicture(
    L"""
    \node {parent} [circle, fill=green, sibling distance = 2.5cm, green]
        child [red] {node {child 1} edge from parent [dashed, green]} 
        child {node [red] {child 2}
        child {node [xshift = -1cm] {grandchild 1}}
        child {node [yshift = .5cm] {grandchild 2}}
        edge from parent [green] node [right, brown] {x}};
    """,
    #options="scale=1",
    preamble="")
end

# ╔═╡ 35950c6b-d4d0-4be2-8b41-786146187c6f
let
  TikzPicture(
    L"""
    \node {parent} [sibling distance = 2.5cm, green]
      child [red] {node {child 1} edge from parent [dashed, green]} 
      child {node [red] {child 2}
      child {node [xshift = -1cm] {grandchild 1}}
      child {node [yshift = .5cm] {grandchild 2}}
      edge from parent [green] node [right, brown] {x}};
    """,
    #options="scale=1",
    preamble="")
end

# ╔═╡ acab0352-d24d-4300-92f5-65beb1e62e00
let
  TikzPicture(
    L"""
    \node [circle, draw=green, inner sep=3ex] {parent} [sibling distance = 1.5cm, green]
      child [red] {node {child 1} edge from parent [dashed, green]} 
      child {node [red] {child 2}
      child {node [xshift = -1cm] {grandchild 1}}
      child {node [yshift = .5cm] {grandchild 2}}
      edge from parent [green] node [right, brown] {x}};
    """,
    #options="scale=1",
    preamble="")
end

# ╔═╡ 09f4b3f1-e7f0-4ab1-9597-0fdbaaf8e615
let
  TikzPicture(
    L"""
    \def\radius{1em}
    \def\sep{10em}
    \def\color{gray}
    \def\sib_dist{7em}
    \node (left) [circle, fill=\color, inner sep=\radius] {} [sibling distance=\sib_dist]
      child [draw=white, line width=0.5mm] { node (left left) [circle, fill=\color, inner sep=\radius] {} edge from parent }
      child [draw=white, line width=0.5mm] { node (left right) [circle, fill=\color, inner sep=\radius] {} edge from parent };

    \node [white, above] at (left.north) {\large $2^{n}$};
    \node [white, above] at (left left.north) {\large $2^{n+1}$};
    \node [white, above] at (left right.north) {\large $2^{n+1}$};

    \node (ellipsis) [\color] at (\sep, 0) {\Huge $\cdots$};
    \node (right) at (2*\sep, 0) [circle, fill=\color, inner sep=\radius] {} [sibling distance=\sib_dist]
      child [draw=white, line width=0.5mm] { node (right left) [circle, fill=\color, inner sep=\radius] {} edge from parent }
      child [draw=white, line width=0.5mm] { node (right right) [circle, fill=\color, inner sep=\radius] {} edge from parent };

    \node [white, above] at (right.north) {\large $2^{n}+k$};
    \node [rectangle, draw=white, white, above] at (right left.north) {\large\textbf ?};
    \node [rectangle, draw=white, white, above] at (right right.north) {\large\textbf ?};
    """,
    options="scale=1.0",
    preamble="")
end

# ╔═╡ 4b4afc4c-ceb3-423f-b4f2-d7688350d812
  # morceaux = TikzPicture(
  #   L"""
  #   \def\d{0.8}
  #   \def\L{10}
  #   \draw[orange, ultra thick] (0,0) -- (\L,0);
  #   \draw[purple, ultra thick] (0,-0.2) -- (0,0.2) node [anchor=south] {$\frac{0}{M-1}$};
  #   \draw[purple, ultra thick] (\d,-0.2) -- (\d,0.2) node [anchor=south] {$\frac{1}{M-1}$};
  #   \draw[purple, ultra thick] (2*\d,-0.2) -- (2*\d,0.2) node [anchor=south] {$\frac{2}{M-1}$};
  #   \draw[purple, ultra thick] (\L/2,-0.2) -- (\L/2,0.2) node [anchor=south] {$\cdots$};
  #   %node (\L/2,0.2) [anchor=south] {$\cdots$};
  #   \draw[purple, ultra thick] (\L,-0.2) -- (\L,0.2) node [anchor=south] {$\frac{M-1}{M-1}$};
  #   \draw[purple, ultra thick] (\L-\d,-0.2) -- (\L-\d,0.2) node [anchor=south] {$\frac{M-2}{M-1}$};
  #   """,
  #   options="scale=1.5",
  #   preamble="",
  # )


# ╔═╡ 00000000-0000-0000-0000-000000000001
PLUTO_PROJECT_TOML_CONTENTS = """
[deps]
LaTeXStrings = "b964fa9f-0449-5b57-a5c2-d3ea65f4040f"
TikzPictures = "37f6aa50-8035-52d0-81c2-5a1d08754b2d"

[compat]
LaTeXStrings = "~1.2.1"
TikzPictures = "~3.4.1"
"""

# ╔═╡ 00000000-0000-0000-0000-000000000002
PLUTO_MANIFEST_TOML_CONTENTS = """
# This file is machine-generated - editing it directly is not advised

[[Artifacts]]
deps = ["Pkg"]
git-tree-sha1 = "c30985d8821e0cd73870b17b0ed0ce6dc44cb744"
uuid = "56f22d72-fd6d-98f1-02f0-08ddc0907c33"
version = "1.3.0"

[[Base64]]
uuid = "2a0f44e3-6c83-55bd-87e4-b1978d98bd5f"

[[Bzip2_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "c3598e525718abcc440f69cc6d5f60dda0a1b61e"
uuid = "6e34b625-4abd-537c-b88f-471c36dfa7a0"
version = "1.0.6+5"

[[Cairo_jll]]
deps = ["Artifacts", "Bzip2_jll", "Fontconfig_jll", "FreeType2_jll", "Glib_jll", "JLLWrappers", "LZO_jll", "Libdl", "Pixman_jll", "Pkg", "Xorg_libXext_jll", "Xorg_libXrender_jll", "Zlib_jll", "libpng_jll"]
git-tree-sha1 = "e2f47f6d8337369411569fd45ae5753ca10394c6"
uuid = "83423d85-b0ee-5818-9007-b63ccbeb887a"
version = "1.16.0+6"

[[Dates]]
deps = ["Printf"]
uuid = "ade2ca70-3891-5945-98fb-dc099432e06a"

[[Expat_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "1402e52fcda25064f51c77a9655ce8680b76acf0"
uuid = "2e619515-83b5-522b-bb60-26c02a35a201"
version = "2.2.7+6"

[[Fontconfig_jll]]
deps = ["Artifacts", "Bzip2_jll", "Expat_jll", "FreeType2_jll", "JLLWrappers", "Libdl", "Libuuid_jll", "Pkg", "Zlib_jll"]
git-tree-sha1 = "35895cf184ceaab11fd778b4590144034a167a2f"
uuid = "a3f928ae-7b40-5064-980b-68af3947d34b"
version = "2.13.1+14"

[[FreeType2_jll]]
deps = ["Artifacts", "Bzip2_jll", "JLLWrappers", "Libdl", "Pkg", "Zlib_jll"]
git-tree-sha1 = "cbd58c9deb1d304f5a245a0b7eb841a2560cfec6"
uuid = "d7e528f0-a631-5988-bf34-fe36492bcfd7"
version = "2.10.1+5"

[[Gettext_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Libiconv_jll", "Pkg", "XML2_jll"]
git-tree-sha1 = "8c14294a079216000a0bdca5ec5a447f073ddc9d"
uuid = "78b55507-aeef-58d4-861c-77aaff3498b1"
version = "0.20.1+7"

[[Glib_jll]]
deps = ["Artifacts", "Gettext_jll", "JLLWrappers", "Libdl", "Libffi_jll", "Libiconv_jll", "Libmount_jll", "PCRE_jll", "Pkg", "Zlib_jll"]
git-tree-sha1 = "04690cc5008b38ecbdfede949220bc7d9ba26397"
uuid = "7746bdde-850d-59dc-9ae8-88ece973131d"
version = "2.59.0+4"

[[InteractiveUtils]]
deps = ["Markdown"]
uuid = "b77e0a4c-d291-57a0-90e8-8db25a27a240"

[[JLLWrappers]]
deps = ["Preferences"]
git-tree-sha1 = "642a199af8b68253517b80bd3bfd17eb4e84df6e"
uuid = "692b3bcd-3c85-4b1f-b108-f13ce0eb3210"
version = "1.3.0"

[[JpegTurbo_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "9aff0587d9603ea0de2c6f6300d9f9492bbefbd3"
uuid = "aacddb02-875f-59d6-b918-886e6ef4fbf8"
version = "2.0.1+3"

[[LZO_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "f128cd6cd05ffd6d3df0523ed99b90ff6f9b349a"
uuid = "dd4b983a-f0e5-5f8d-a1b7-129d4a5fb1ac"
version = "2.10.0+3"

[[LaTeXStrings]]
git-tree-sha1 = "c7f1c695e06c01b95a67f0cd1d34994f3e7db104"
uuid = "b964fa9f-0449-5b57-a5c2-d3ea65f4040f"
version = "1.2.1"

[[LibGit2]]
deps = ["Printf"]
uuid = "76f85450-5226-5b5a-8eaa-529ad045b433"

[[Libdl]]
uuid = "8f399da3-3557-5675-b5ff-fb832c97cbdb"

[[Libffi_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "a2cd088a88c0d37eef7d209fd3d8712febce0d90"
uuid = "e9f186c6-92d2-5b65-8a66-fee21dc1b490"
version = "3.2.1+4"

[[Libgcrypt_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Libgpg_error_jll", "Pkg"]
git-tree-sha1 = "b391a18ab1170a2e568f9fb8d83bc7c780cb9999"
uuid = "d4300ac3-e22c-5743-9152-c294e39db1e4"
version = "1.8.5+4"

[[Libgpg_error_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "ec7f2e8ad5c9fa99fc773376cdbc86d9a5a23cb7"
uuid = "7add5ba3-2f88-524e-9cd5-f83b8a55f7b8"
version = "1.36.0+3"

[[Libiconv_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "cba7b560fcc00f8cd770fa85a498cbc1d63ff618"
uuid = "94ce4f54-9a6c-5748-9c1c-f9c7231a4531"
version = "1.16.0+8"

[[Libmount_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "51ad0c01c94c1ce48d5cad629425035ad030bfd5"
uuid = "4b2f31a3-9ecc-558c-b454-b3730dcb73e9"
version = "2.34.0+3"

[[Libtiff_jll]]
deps = ["Artifacts", "JLLWrappers", "JpegTurbo_jll", "Libdl", "Pkg", "Zlib_jll", "Zstd_jll"]
git-tree-sha1 = "291dd857901f94d683973cdf679984cdf73b56d0"
uuid = "89763e89-9b03-5906-acba-b20f662cd828"
version = "4.1.0+2"

[[Libuuid_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "f879ae9edbaa2c74c922e8b85bb83cc84ea1450b"
uuid = "38a345b3-de98-5d2b-a5d3-14cd9215e700"
version = "2.34.0+7"

[[LittleCMS_jll]]
deps = ["JpegTurbo_jll", "Libdl", "Libtiff_jll", "Pkg"]
git-tree-sha1 = "e6ea89d915cdad8d264f7f9158c6664f879edcde"
uuid = "d3a379c0-f9a3-5b72-a4c0-6bf4d2e8af0f"
version = "2.9.0+0"

[[Logging]]
uuid = "56ddb016-857b-54e1-b83d-db4d58db5568"

[[Markdown]]
deps = ["Base64"]
uuid = "d6f4376e-aef5-505a-96c1-9c027394607a"

[[OpenJpeg_jll]]
deps = ["Libdl", "Libtiff_jll", "LittleCMS_jll", "Pkg", "libpng_jll"]
git-tree-sha1 = "e330ffff1c6a593fa44cc40c29900bee82026406"
uuid = "643b3616-a352-519d-856d-80112ee9badc"
version = "2.3.1+0"

[[PCRE_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "1b556ad51dceefdbf30e86ffa8f528b73c7df2bb"
uuid = "2f80f16e-611a-54ab-bc61-aa92de5b98fc"
version = "8.42.0+4"

[[Pixman_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "6a20a83c1ae86416f0a5de605eaea08a552844a3"
uuid = "30392449-352a-5448-841d-b1acce4e97dc"
version = "0.40.0+0"

[[Pkg]]
deps = ["Dates", "LibGit2", "Libdl", "Logging", "Markdown", "Printf", "REPL", "Random", "SHA", "UUIDs"]
uuid = "44cfe95a-1eb2-52ea-b672-e2afdf69b78f"

[[Poppler_jll]]
deps = ["Artifacts", "Cairo_jll", "Fontconfig_jll", "Glib_jll", "JLLWrappers", "JpegTurbo_jll", "Libdl", "Libtiff_jll", "OpenJpeg_jll", "Pkg", "libpng_jll"]
git-tree-sha1 = "e11443687ac151ac6ef6699eb75f964bed8e1faa"
uuid = "9c32591e-4766-534b-9725-b71a8799265b"
version = "0.87.0+2"

[[Preferences]]
deps = ["TOML"]
git-tree-sha1 = "00cfd92944ca9c760982747e9a1d0d5d86ab1e5a"
uuid = "21216c6a-2e73-6563-6e65-726566657250"
version = "1.2.2"

[[Printf]]
deps = ["Unicode"]
uuid = "de0858da-6303-5e67-8744-51eddeeeb8d7"

[[REPL]]
deps = ["InteractiveUtils", "Markdown", "Sockets"]
uuid = "3fa0cd96-eef1-5676-8a61-b3b8758bbffb"

[[Random]]
deps = ["Serialization"]
uuid = "9a3f8284-a2c9-5f02-9a11-845980a1fd5c"

[[Requires]]
deps = ["UUIDs"]
git-tree-sha1 = "4036a3bd08ac7e968e27c203d45f5fff15020621"
uuid = "ae029012-a4dd-5104-9daa-d747884805df"
version = "1.1.3"

[[SHA]]
uuid = "ea8e919c-243c-51af-8825-aaa63cd721ce"

[[Serialization]]
uuid = "9e88b42a-f829-5b0c-bbe9-9e923198166b"

[[Sockets]]
uuid = "6462fe0b-24de-5631-8697-dd941f90decc"

[[TOML]]
deps = ["Dates"]
git-tree-sha1 = "44aaac2d2aec4a850302f9aa69127c74f0c3787e"
uuid = "fa267f1f-6049-4f14-aa54-33bafae1ed76"
version = "1.0.3"

[[Tectonic]]
deps = ["Pkg"]
git-tree-sha1 = "acf12eccb390a78653ee805cd527898f01f78a85"
uuid = "9ac5f52a-99c6-489f-af81-462ef484790f"
version = "0.6.1"

[[TikzPictures]]
deps = ["LaTeXStrings", "Poppler_jll", "Requires", "Tectonic"]
git-tree-sha1 = "a08671c0979063a437378f6410bb75a465f3cd1c"
uuid = "37f6aa50-8035-52d0-81c2-5a1d08754b2d"
version = "3.4.1"

[[UUIDs]]
deps = ["Random", "SHA"]
uuid = "cf7118a7-6976-5b1a-9a39-7adc72f591a4"

[[Unicode]]
uuid = "4ec0a83e-493e-50e2-b9ac-8f72acf5a8f5"

[[XML2_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Libiconv_jll", "Pkg", "Zlib_jll"]
git-tree-sha1 = "be0db24f70aae7e2b89f2f3092e93b8606d659a6"
uuid = "02c8fc9c-b97f-50b9-bbe4-9be30ff0a78a"
version = "2.9.10+3"

[[XSLT_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Libgcrypt_jll", "Libgpg_error_jll", "Pkg", "XML2_jll"]
git-tree-sha1 = "2b3eac39df218762d2d005702d601cd44c997497"
uuid = "aed1982a-8fda-507f-9586-7b0439959a61"
version = "1.1.33+4"

[[Xorg_libX11_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libxcb_jll", "Xorg_xtrans_jll"]
git-tree-sha1 = "5be649d550f3f4b95308bf0183b82e2582876527"
uuid = "4f6342f7-b3d2-589e-9d20-edeb45f2b2bc"
version = "1.6.9+4"

[[Xorg_libXau_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "4e490d5c960c314f33885790ed410ff3a94ce67e"
uuid = "0c0b7dd1-d40b-584c-a123-a41640f87eec"
version = "1.0.9+4"

[[Xorg_libXdmcp_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "4fe47bd2247248125c428978740e18a681372dd4"
uuid = "a3789734-cfe1-5b06-b2d0-1dd0d9d62d05"
version = "1.1.3+4"

[[Xorg_libXext_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libX11_jll"]
git-tree-sha1 = "b7c0aa8c376b31e4852b360222848637f481f8c3"
uuid = "1082639a-0dae-5f34-9b06-72781eeb8cb3"
version = "1.3.4+4"

[[Xorg_libXrender_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libX11_jll"]
git-tree-sha1 = "19560f30fd49f4d4efbe7002a1037f8c43d43b96"
uuid = "ea2f1a96-1ddc-540d-b46f-429655e07cfa"
version = "0.9.10+4"

[[Xorg_libpthread_stubs_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "6783737e45d3c59a4a4c4091f5f88cdcf0908cbb"
uuid = "14d82f49-176c-5ed1-bb49-ad3f5cbd8c74"
version = "0.1.0+3"

[[Xorg_libxcb_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "XSLT_jll", "Xorg_libXau_jll", "Xorg_libXdmcp_jll", "Xorg_libpthread_stubs_jll"]
git-tree-sha1 = "daf17f441228e7a3833846cd048892861cff16d6"
uuid = "c7cfdc94-dc32-55de-ac96-5a1b8d977c5b"
version = "1.13.0+3"

[[Xorg_xtrans_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "79c31e7844f6ecf779705fbc12146eb190b7d845"
uuid = "c5fb5394-a638-5e4d-96e5-b29de1b5cf10"
version = "1.4.0+3"

[[Zlib_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "320228915c8debb12cb434c59057290f0834dbf6"
uuid = "83775a58-1f1d-513f-b197-d71354ab007a"
version = "1.2.11+18"

[[Zstd_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "2c1332c54931e83f8f94d310fa447fd743e8d600"
uuid = "3161d3a3-bdf6-5164-811a-617609db77b4"
version = "1.4.8+0"

[[libpng_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Zlib_jll"]
git-tree-sha1 = "6abbc424248097d69c0c87ba50fcb0753f93e0ee"
uuid = "b53b4c65-9356-5827-b1ea-8c7a1a84506f"
version = "1.6.37+6"
"""

# ╔═╡ Cell order:
# ╠═882c47a6-13c5-11ec-2eee-5f38073a3824
# ╠═0391208b-b2ab-4240-a681-37bc7ded21ab
# ╟─52dfc51b-bcc7-44ed-93f3-5a616cb7ac5d
# ╠═9734ee4b-1a80-4de0-8293-cfd7817663b6
# ╠═06e834ff-8904-46a6-b554-014ca15541c9
# ╠═35950c6b-d4d0-4be2-8b41-786146187c6f
# ╠═acab0352-d24d-4300-92f5-65beb1e62e00
# ╠═09f4b3f1-e7f0-4ab1-9597-0fdbaaf8e615
# ╟─4b4afc4c-ceb3-423f-b4f2-d7688350d812
# ╟─00000000-0000-0000-0000-000000000001
# ╟─00000000-0000-0000-0000-000000000002
