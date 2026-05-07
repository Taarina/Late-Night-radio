import ThoughtInput from "./ThoughtInput";

export default function MoodScreen() {
  return (
    <div
      style={{
        minHeight: "100vh",
        backgroundImage:
          "url('https://images.unsplash.com/photo-1506744038136-46273834b3fb')",
        backgroundSize: "cover",
        backgroundPosition: "center",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        padding: "2rem",
      }}
    >
      <div
        style={{
          width: "100%",
          maxWidth: "700px",
          background: "rgba(0,0,0,0.6)",
          backdropFilter: "blur(10px)",
          padding: "3rem",
          borderRadius: "20px",
        }}
      >
        <h1
          style={{
            fontSize: "3rem",
            marginBottom: "1rem",
            textAlign: "center",
          }}
        >
          Late Night Radio
        </h1>

        <p
          style={{
            textAlign: "center",
            marginBottom: "3rem",
            opacity: 0.7,
          }}
        >
          Pick a mood. Leave a thought. Let the night keep you company.
        </p>

        <iframe
          style={{
            borderRadius: "12px",
            marginBottom: "3rem",
          }}
          src="https://open.spotify.com/embed/playlist/37i9dQZF1DX7qK8ma5wgG1?utm_source=generator"
          width="100%"
          height="352"
          frameBorder="0"
          allowFullScreen
          allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
          loading="lazy"
        />

        <ThoughtInput />
      </div>
    </div>
  );
}
