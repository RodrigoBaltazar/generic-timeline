<?php

namespace App\Http\Controllers;

use App\Models\Video;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Inertia\Inertia;
use Inertia\Response;

class VideoController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index(): Response 
    {
        return Inertia::render('Videos/Index', [

            'videos' => Video::with('user:id,name')->latest()->get(),
        ]);
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request): RedirectResponse
    {
        $validated = $request->validate([

            'message' => 'required|string|max:255',
            'title' => 'required|string|max:255',
            'duration' => 'required|integer',
            'description' => 'required|string|max:255',
            'file_path' => 'required|string|max:255',

        ]);

 

        $request->user()->videos()->create($validated);

 

        // return redirect(route('videos.index'));    } Troquei após salvar o vídeo ao invés de continuar na página de salvar mais vídeos, ir
        //para página de dashboard para podermos já ver o vídeo exibindo
            return redirect(route('Dashboard.index'));
    }

    /**
     * Display the specified resource.
     */
    public function show(Video $video)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Video $video)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Video $video): RedirectResponse    {
        $this->authorize('update', $video);

 

        $validated = $request->validate([

            'message' => 'required|string|max:255',
            'title' => 'required|string|max:255',
            'duration' => 'required|integer',
            'description' => 'required|string|max:255',
            'file_path' => 'required|string|max:255',

        ]);

 

        $video->update($validated);

 

        return redirect(route('videos.index'));
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Video $video): RedirectResponse    
    {
        $this->authorize('delete', $video);

 

        $video->delete();

 

        return redirect(route('videos.index'));
    }
}
