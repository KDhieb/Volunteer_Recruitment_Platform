

function classColor(c) {
    if (c === "One-time") {
        return "bg-success text-white badge py-2 px-4"
    } else if (c === "Weekly") {
        return "bg-danger text-white badge py-2 px-4"
    } else
        return "bg-warning text-white badge py-2 px-4"
}